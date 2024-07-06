#include<iostream>
#include <SDL2/SDL.h>
using namespace std;

int main (int argc, char *argv[]){
  SDL_Init(SDL_INIT_EVERYTHING);
  SDL_Window *window = SDL_CreateWindow("Hello SDL Window", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 600, 800, SDL_WINDOW_ALLOW_HIGHDPI);

  if (window == NULL){
    cout<<"Error";
    return 1;
  }

  SDL_Event windowEvent;

  while (true){
    if (SDL_PollEvent(&windowEvent)){
      if(SDL_QUIT == windowEvent.type){
        break;
      }
    }
  }

  SDL_DestroyWindow(window);
  SDL_Quit();
  return EXIT_SUCCESS;
}